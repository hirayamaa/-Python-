import re

names_regex = re.compile(r'Agent \w+')
# 「Agent 名前」を置き換える
print(names_regex.sub('CENSORED',
                      'Agent Alice gave the secret documents to Agent Bob.'))

AGENT_TEXT = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agent_name_regex = re.compile(r'Agent (\w)\w*')
print(agent_name_regex.search(AGENT_TEXT).group(1))
# 名前の頭文字だけ表示する
# A**** told C**** that E**** knew B**** was a double agent.
print(agent_name_regex.sub(r'\1****', AGENT_TEXT))

