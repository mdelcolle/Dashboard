from jira import JIRA
import clases as c
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

jira = JIRA(
  basic_auth=("u623442", "!!Fluxit2021"), 
  options={
    'server': "https://gestioncio.telecom.com.ar/"
  }
)


issues = jira.search_issues('Sprint = 2925 AND component = Celula1 AND type = Story')
list = []

for issue in issues:
    h = c.history(
      issue.fields.summary,
      issue.fields.assignee.displayName,
      issue.fields.customfield_10106, #StoryPoints
      issue.fields.customfield_10377, #Epica
      issue.fields.status.name)
    list.append(h)

labelsAssignee = [x.as_lbl_assignee() for x in list]
labelsEpic = [x.as_lbl_epic() for x in list]
labelsStatus = [x.as_lbl_status() for x in list]
values = [x.as_values_points() for x in list]

#specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain','colspan':2}, {}]]
fig = make_subplots(rows=2, cols=2, specs=specs)


fig.add_trace(go.Pie(labels=labelsAssignee, values=values, name="PC x Usuario"),1, 1)
fig.add_trace(go.Pie(labels=labelsStatus, values=values, name="PC x Status"),1, 2)
fig.add_trace(go.Pie(labels=labelsEpic, values=values, name="PC x Epica"),2, 1)


fig.update_traces(hole=.4,textposition='inside',hoverinfo='label+percent+value', textinfo='label+value')


fig.update_layout(title_text="C1 - Reporte de Sprint 36")
fig.show()
