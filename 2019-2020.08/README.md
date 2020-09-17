README

11. [11_baekjoon_17822](./11_baekjoon_17822.py)

    - 문제 푼 시간: 59m
    
    - 117920/ 276
    
    - 전체적으로 회전 - 같은 수 찾기 - 삭제 or 보강이 반복된다.
    
    - 같은수를 찾을 때, idex= 0 과 idex =M 도 고려 해야한다.
    
    -  문제에서 x 표시 한 것을 0 으로 표시하고 풀었는데, 이때 해당 칸을 고려하지 않도록 코드를 짜야한다. (cnt나 보강시 고려해서는 안됨)
    
    - 나누기 할 때, **분모가 0**인 경우를 고려할 것! (런타임에러가 난다. ㅜㅜ)
    
    - 다른 사람의 코드 중에는 나누기 대신, 곱하기로 검사한 사람이 있었다.
    
      ```python
      if onepan[i][j] * cnt > total:
          onepan[i][j] -= onepan[i][j]
      elif onepan[i][j] * cnt < total:
          onepan[i][j] += onepan[i][j]
      ```
    
      이런식으로 하면, 에러날 일이 없다! 


​    

13. [13_baekjoon_10844](./13_baekjoon_10844.py)
- 115436/140
  - 처음에는 dfs로 풀었다가, 시간초과가 났다. 
    
    - dp memoization을 써야하는 문제.. ! 
    
    - 예외처리에 대해서 고민해봐야 한다.
    
    - top-down 방식으로 풀이할 수 도 있다. (잘 이해가 안된다.)

14. [14_baekjoon_16235](./14_baekjoon_16235.py) 🌟🌟
    - 문제 푼 시간 : 2h 17m 했지만... 못풀었다...😭
    
    - 1000번이라면, 죽은 나무와 살아있는 나무를 분리해서 생각 했어야함..!
    
    - 인덱스가 어디서 시작 하는 지 체크!
    
    - [참고](https://dailyheumsi.tistory.com/60) 해서 코드를 다시 짜보았다.
    
    - deque를 이용해서 dict_map을 그리는 방법이 유용함...!
    
    - 그럼에도 불구하고 시간초과가 뜬다.. (37%에서..)..😭
    
    - `fall`에서 반복되는 반복문을 하나 줄였더니 통과되었다 ! ! 
    
15. [15_baekjoon_17779](./15_baekjoon_17779.py)🌟🌟🌟🌟
    
    - 문제 푼 시간: 1h 31m 했지만.. 포기... ㅜ ㅜ 인덱스가 너무 복잡하다..
    - 여전히 문제를 읽고 이해하는데 엄청 오랜 시간이 걸린다....
    - 포기.... 다음에 다시 풀어보기 !
    - 새롭게 짠 전략 -> 문제를 5분안에 한 번 다 읽고, 로드가 있을 것 같은 부분을 체크하기!
    - 117388/284
    
16. [16_baekjoon_13450](./16_baekjoon_13450)
    - 방법 감을 아예 못 잡음.. 당분간 간단한 문제 풀기!
    - idea는 bfs로 4방향을 돌면서 움직이고, 방향 바꾼 횟수를 카운트 해주는 것!

17. [17_swea_4615](./17_swea_4615.py)
    
    - 대각선 방향 설정 잘해주기 ! 
    
18. [18_swea_4613](./18swea_4613.py) 🌟

    - 처음에 재귀로 풀 생각하다가 엄청 오래 푼 문제 ㅜㅜ 

    - 어림잡아 최악의 경우는 3^48이기 때문에(물론 이것보다는 조금 적지만)

      얼핏 생각해도 재귀는 안된다고 판단해야한다 ㅜㅜ 

    - 계산 해보고 배열로 풀어야 겠다고 마음먹었어야....

    - 여전히 한참 손에 안익네..

25. [25_swea_1824](./25_swea_1824.py)
    
    - 루프를 자르는 완료조건을 잘 생각할 것 (같은 좌표고, 방향, 메모하는 값이 같다면 루프이다 !)
    - 재귀로 짜다가... 스택으로 짜다가.. 난리법석
    
20. [26_swea_1244](./26_swea_1244.py)

    - 현재 위치에서 바꿀 것 하나만 뽑으면 됨.
    - dfs 돌면서, 복원해야하는지 잘 생각할 것 ! 
    - 복원 해야하는 경우, 함수의 인자로 넣으면 따로 복원할 필요가 없다!


27. [27_swae_1210](./27_swea_1210.py)

    - while문 조건 검사 시, 0일 때 빠져나오므로 1일때까지 위치를 알려면 값을 한번 빼줘야 함.

      

28. [28_swea_1249](./28_swea_1249.py)
    
    - 처음에 dfs 재귀로 풀었더니 시간초과 
    
    - visited에 해당 좌표까지 가는데 걸리는 최소 비용을 저장
    
    - 값을 저장하기 때문에 cost를 들고 다닐 필요가 없음 ! 
    
      (해당 좌표가 두번 일 수도 있고, 다른 방향으로 접근, 갱신 되어 그 cost가 최소가 아닐 수도 있음 )

34. [34_swea_2814](./34_swea_2814.py)
    - dfs로 재귀로 짤 때, O(n)을 계산해야하는데.. 
    - 최장 거리 할 때, 복원 비복원 생각 잘 할 것!
35. [35_swea_1808](./35_swea_1808.py) 🌟🌟
    
- 다시 풀기 ! 
  
37. [37_swea_1226](./37_swea_1226.py)
    
    - 처음에 bfs로 3에도 갈 수 있는것을 생각 안했었다.

64. [64_baekjoon_17070](./64_baekjoon_17070.py)

    - 처음에 dfs 로 풀었는데, 시간 초과가 나서 dp 로 풀었다.

    - 처음부터 dp 라고 생각하면 간단히 해결 할 수 있다. 

    - 오른쪽: 이전에 오른쪽이거나, 대각선

      왼쪽: 이전에 세로였거나, 대각선

      대각선: 이전에 오른쪽, 아래, 대각선

65. [65_baekjoon_17136](./65_baekjoon_17136.py)
    - 처음에 너무 그리디하게 생각함. 구글링 해보니 나같은 실수를 한 사람이 많았다 
    - dfs 2차원으로 돌릴때 좌표 유의하기 
    - 최대까지 돌기전에 한번 검사하고 들어가면 빠르다 (28번줄)

67. [67_baekjoon_15649](./67_baekjoon_15649) 15:40
    - 단순한 문제인데, 생각보다 시간이 걸렸다 !
    - 그래프 그려보고, N과 M은 진짜 많이 반복해서 풀어야 겠다.

41. [68_baekjoon-15684](./68_baekjoon-15684) 01:53
    
    - 시간초과... 

69. [69_swea_2112](./69_swea_2112.py)  01:18 -> 다시 풀기
    
    - 필름 확인하는 로직 짜는데 오랜 시간이 걸림... W,D를 헷갈려서.. 
    - copy, deepcopy 문제로 오류가 났음 (dfs 그래프 그려보고 하기)

70. [70_baekjoon_14499](./70_baekjoon_14499.py) 28:04
    
    - 동서남북이 아니고, 동서 북남인것 주의 
    - 주사위 그리는 것 주의
    - 바깥으로 나간거 체크하면서 x, y 복원 시켜주기

71. [71_baekjoon_14891](./71_baekjoon_14891.py) 01:24

    - 나는 무조건 회전하는걸 생각 못함... ㅎ ....
- 조건 확인 좀 잘하자 ㅠㅠ 

72. [72_baekjoon_15662](./72_baekjoon_15662.py) 36:04
    - 인덱스 처리 유의 하기(한번 그려보고 할 것) 
    - 범위 마지막은 미만인 것을 유의
73. [73_baekjoon_14503](./73_baekjoon_14503.py) 48:08
    - 꼭 다시 풀어보기... 
    - 생각을 잘못한건가..방향을 줬다는 것에 대해 생각해보기
    - 방향에 따라 분기 한다 -> 조건이 더 많은 것 부터 검사한다.
74. [74_baekjoon_14890](./74_baekjoon_14890)  01:06
    - 한 줄씩 생각하기 
    - l개를 봐야하면 범위 잘 생각하기
75. [75_baekjoon_뱀](./75_baekjoon_뱀.py) 53:41
    - 1초일때 방향 변환의 의미를 몰랐다.. 
    - 지나고 나서 바꾸고 언제 초를 더해줘야하는지 잘 생각할 것
76. [76_baekjoon_드래곤커브](./76_baekjoon_드래곤커브.py) 1 : 00 -> 못품..
    
    - 똑바로 그림 그려 보고 하기 ( 그러니까 아침에 한 문제를 풀어야한다..ㅜㅜ 저녁에 2개만 풀 수 있도록) 
77. [77_baekjoon_미네랄](./77_baekjoon_미네랄.py) 1:28

    - 처음에 문제 이해하는데 오래 걸림 .. 

    - 왜 틀렸다고 나오는지 모르겠다.. 
78. [78_baekjoon_테트로미노](./78_baekjoon_테트로미노.py) 
    - dfs 그림 그려보고 잘 생각하기
    
    - o(19 * n* m) = 19 * 250000
82. [82_baekjoon_감시](./82_baekjoon_감시.py)
    

    - CCTV는 CCTV를 통과할 수 있다. 조건을 놓칠 뻔 했다
    - 감시 카메라의 경우의수가 제일 중요 8 ^ 4 = 2 ^ 16 = 약 6만개 ..
    - -> 방향 모듈러로 검사하는 거로도 풀어보기 !
80. [83_baekjoon_사다리조작](./83_baekjoon_사다리조작.py)
    - 세세하게 단위별로 예를 생각해서 구현 하기
    - 범위 헷갈리는 문제.. 
    - o(270 ** 3)
81. [84_baekjoon_치킨배달](./84_baekjoon_치킨배달.py)
    - 순열이 아니고 조합 문제! ! 순열로 짜면 시간 초과가 난다.
82. [91_baekjoon_두동전](./91_baekjoon_두동전)
    - 10번까지 눌러도 된다는 말은, 1~10까지는 최소값을 업데이트 해줘도 대고, 11번쨰부터 안되는 거니까 > 10 으로 해줘야함

109. [109_baekjoon_1048(easy)](./10911_baekjoon_1048(easy).py)
    - t.append 한 후에 복사를 하지 않고 pop을 하면 원래 board에 반영된다. (복사 해주어야함, 1차원이라서 얕은 복사 가능)
    - `한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다.` 말의 의미를 유의 할 것
    - `0` 처리 해주기, Line을 만들 때 0이 아닌 것만 담아준다. (조건 검사 유의)
    - 회전 시 인덱스 처리