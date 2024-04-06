import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)


## 1부터 1000001까지 비교하면서 고장난 숫자가 있을 경우에는 패스하는 식으로 하나씩 모두 검증
## 주어진 숫자는 500000까지 였지만 갈 수 있는 숫자는 더 높기때문에 1000000까지로 설정


