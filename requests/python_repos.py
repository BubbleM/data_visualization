import requests

# 执行ＡＰＩ调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars/'
# 将API响应存储在一个变量r中
r = requests.get(url)
print("Status code:",r.status_code)

# API返回的JSON格式的信息，使用json()将这些信息转换为一个字典
response_dict = r.json()
print(response_dict.keys()) # dict_keys(['items', 'total_count', 'incomplete_results'])

print("Total repositoroes:",response_dict['total_count'])

# 探索仓库相关信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
# 	print(key)
print("\nSelected information about first repository:")
# print("Name:",repo_dict['name'])
# print("Owner:",repo_dict['owner']['login'])
# 循环打印API调用返回的每个仓库的特定信息
for repo_dict in repo_dicts:
	print("Name:",repo_dict['name'])
	print("Owner:",repo_dict['owner']['login'])