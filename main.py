from jira import JIRA
import clases as c
import plotly.express as px
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go
import pandas as pd




jira = JIRA(
  basic_auth=("u623442", "!!Fluxit2021"), 
  options={
    'server': "https://gestioncio.telecom.com.ar/"
  }
)


issues = jira.search_issues('Sprint = 2810 AND component = Celula1 AND type = Story')
list = []


for issue in issues:
    h = c.history(
      issue.fields.summary,
      issue.fields.assignee.displayName,
      issue.fields.customfield_10106, #StoryPoints
      issue.fields.customfield_10377, #Epica
      issue.fields.status)
    list.append(h)
#df = pd.DataFrame(list)

df = pd.DataFrame([x.as_dict() for x in list])


fig = px.pie(df,values='storypoints',names='epiclink',title='Puntos por epica')

#fig.add_trace(px.pie(df,values='storypoints',names='epiclink',title='Puntos por epica'))
#fig.add_trace(px.pie(df,values='storypoints',names='assignee',title='Puntos por usuario'))

fig.update_traces(textposition='inside', textinfo='percent+label')
#fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.show()





