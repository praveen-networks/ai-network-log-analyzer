from openai import OpenAI

client = OpenAI()

log_data = """
[10:01] AP1 - Client disconnected - Signal weak
[10:10] AP1 - High channel interference detected
[10:15] AP1 - Client dropped - High load
"""

prompt = f"""
Analyze the following network logs and identify issues and possible solutions:

{log_data}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
