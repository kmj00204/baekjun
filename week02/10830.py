MOD = 1000  # 행렬 원소가 항상 1000으로 나눈 나머지로 주어지므로


# 행렬 곱셈 함수
def matrix_multiply(A, B, size):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(size)) % MOD
    return result


# 행렬 거듭제곱 함수
def matrix_pow(A, B, size):
    # 단위 행렬 생성
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = A

    while B > 0:
        if B % 2 == 1:  # B가 홀수일 경우
            result = matrix_multiply(result, base, size)
        base = matrix_multiply(base, base, size)
        B //= 2

    return result


# 입력 받기
N, B = map(int, input().split())  # 행렬의 크기 N, 거듭제곱 횟수 B
matrix = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B번 제곱 계산
result_matrix = matrix_pow(matrix, B, N)

# 결과 출력
for row in result_matrix:
    print(*row)
