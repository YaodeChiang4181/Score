def analyze_scores():
    score_input = input("請輸入一串成績，以空格分隔（例如：85 72 45 60 91）： ")
    scores_str = score_input.split()

    failing_count = 0
    valid_scores = []
    total_score = 0
    max_grade = -1  # Initialize with a value lower than any possible score
    min_grade = 101 # Initialize with a value higher than any possible score

    for score_s in scores_str:
        try:
            score = int(score_s)
            if 0 <= score <= 100:
                valid_scores.append(score)
                total_score += score

                if score < 60:
                    failing_count += 1

                if score > max_grade:
                    max_grade = score
                if score < min_grade:
                    min_grade = score
            else:
                print(f"警告：分數 {score} 不在 0 到 100 的有效範圍內，將忽略此分數。")
        except ValueError:
            print(f"警告：'{score_s}' 不是有效的數字，將忽略此輸入。")

    print(f"\n此串成績中不及格的數量為：{failing_count}")

    if valid_scores:
        average_score = total_score / len(valid_scores)
        print(f"此串有效成績的平均數為：{average_score:.2f}")
        print(f"此串成績中的最大成績為：{max_grade}")
        print(f"此串成績中的最小成績為：{min_grade}")
    else:
        print("沒有有效的成績可以計算平均數、最大值和最小值。")

# 執行函數
analyze_scores()