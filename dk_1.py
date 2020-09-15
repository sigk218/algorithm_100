# 하나의 에이전트는 최대 3개의 티켓
# 절차에 따라 에이전트를 찾을 수 없는 경우는 throw NoAgentFoundException

# 새로운 티켓을 위해 두가지 정택이 있다
# 티켓 : id, 상세
# 에이전트 : 이름, 기술, 현재 에이전트에게 할당된 수
# 에이전트에게 티켓을 매칭할 수 있는 최적의 알고리즘

from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self._name)

    def __init__(self, name, skills, load):
        self._name = name
        self._skills = skills
        self._load = load

    @property
    def name(self):
        return self._name

    @property
    def load(self):
        return self._load

    @property
    def skills(self):
        return self._skills


class Ticket(object):
    def __init__(self, id, restrictions):
        self._id = id
        self._restrictions = restrictions

    @property
    def id(self):
        return self._id

    @property
    def restrictions(self):
        return self._restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        # 가장 최근에 로드된 에이전트, 기술은 매치할 필요 x
        if len(agents) < 1:
            raise NoAgentFoundException
        try:
            loaded_agents = [agent for agent in agents if agent.load < 4]
            if len(loaded_agents) < 1: raise NoAgentFoundException
            return sorted(loaded_agents, key=lambda agent: agent.load)[0]
        except:
            raise NoAgentFoundException


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:

        if len(agents) < 1: raise NoAgentFoundException
        try:
            flexible_agent = [[len(set(agent._skills) - set(ticket.restrictions)), agent] for agent in agents if set(ticket.restrictions) & set(agent.skills)]
            if len(flexible_agent) < 1: raise NoAgentFoundException
            return sorted(flexible_agent, key=lambda agent: (len(agent[1].skills), agent[1].load))[0][1]
        except:
            raise NoAgentFoundException

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
agent3 = Agent(name="C", skills=["English"], load=4)


least_loaded_policy = LeastLoadedAgent()
re = least_loaded_policy.find(ticket, [agent1, agent2, agent3])

least_flexible_policy = LeastFlexibleAgent()
# least_flexible_policy.find(ticket, [])