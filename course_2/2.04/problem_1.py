# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

with open("problem_1_dataset.txt") as old, open("problem_1_dataset_processed.txt", "w") as new:
    new.write('\n'.join(old.read().split('\n')[::-1]))
