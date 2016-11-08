from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.taskList, name='index'),

    # task

    #url(r'^tasks$', views.taskList, name='index'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.TaskDetailView.as_view(), name='taskDetail'),
    url(r'^tasks/add$', views.taskAdd, name='taskAdd'),
    url(r'^tasks/create$', views.taskCreate, name='taskCreate'),
    url(r'^tasks/(?P<task>[0-9]+)/edit$', views.taskEdit, name='taskEdit'),
    url(r'^tasks/(?P<task>[0-9]+)/update$', views.actionTaskUpdate, name='actionTaskUpdate'),
    url(r'^tasks/(?P<task>[0-9]+)/delete$', views.deleteTask, name='deleteTask'),

    url(r'^tasks/(?P<task>[0-9]+)/checklist$', views.checklistTask, name='checklistTask'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/(?P<check>[0-9]+)$', views.CheckDetailView, name='checkDetail'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/add$', views.checkAdd, name='checkAdd'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/addExisting$', views.checkAddExisting, name='checkAddExisting'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/addExistingAction$', views.checkAddExistingAction, name='checkAddExistingAction'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/create$', views.checkCreate, name='checkCreate'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/edit', views.checkListEdit, name='checkListEdit'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/update', views.checkListUpdate, name='checkListUpdate'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/(?P<check>[0-9]+)/delete$', views.checkDelete, name='checkDelete'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/(?P<check>[0-9]+)/edit$', views.checkEdit, name='checkEdit'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/(?P<check>[0-9]+)/update$', views.checkUpdate, name='checkUpdate'),
    url(r'^tasks/(?P<task>[0-9]+)/checklist/(?P<check>[0-9]+)/delete$', views.checkDelete, name='checkDelete'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/stateEdited$', views.editStates,
        name='editStates'),




    url(r'^tasks/(?P<task>[0-9]+)/solution_list$', views.TaskSolutionList, name='TaskSolutionList'),
    url(r'^tasks/solution_list$', views.AllSolutionList, name='AllSolutionList'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)$', views.solutionDetaiView, name='SolutionDetail'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/checkListFill$', views.checkListFill,
        name='checkListFill'),
    # url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/feedback', views.feedbackDetail, name='FeedbackDetail'),
    # url(r'^tasks/(?P<task>[0-9]+)/solution_list/add$', views.solutionAddAmount, name='SolutionAdd'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/add$', views.solutionAdd, name='SolutionAdd'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/update$', views.solutionUpdate,
        name='SolutionUpdate'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/action_update$', views.actionSolutionUpdate,
        name='actionSolutionUpdate'),
    url(r'^tasks/(?P<task>[0-9]+)/solution/create$', views.solutionCreate, name='SolutionCreate'),
    url(r'^tasks/solution/(?P<solution>[0-9]+)/delete$', views.solutionDelete
    , name='SolutionDelete'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/delete$', views.solutionDeleteTasked,
        name='SolutionDeleteTasked'),

    # checklist

    # url(r'^checklists$', views.checklistList, name='checklistList'),
    # url(r'^checklists/(?P<checklist>[0-9]+)$', views.checklistDetailView.as_view(), name='checklistDetail'),
    # url(r'^checklists/(?P<checklist>[0-9]+)/add$', views.checklistAdd, name='checklistDetail'),
    url(r'^checklists/add$', views.checkListAdd, name='checkListAdd'),
    url(r'^checklists/create$', views.checkListCreate, name='checkListCreate'),
    url(r'^checklists/(?P<checklist>[0-9]+)/delete$', views.checkListDelete, name='checkListDelete'),

    # check

    # url(r'^checks$', views.checkList, name='checkList'),
    # url(r'^checks/(?P<check>[0-9]+)$', views.checkDetailView.as_view(), name='checkDetail'),
    url(r'^checks/add$', views.checkAddNoTask, name='checkAddNoTask'),
    url(r'^checks/create$', views.checkCreateNoTask, name='checkCreateNoTask'),
    # url(r'^checks/(?P<check>[0-9]+)/edit$', views.checkEdit, name='checkEdit'),
    # url(r'^checks/(?P<check>[0-9]+)/update$', views.checkUpdate, name='checkUpdate'),
    # url(r'^checks/(?P<check>[0-9]+)/delete$', views.checkDelete, name='checkDelete'),

    # solution

    # url(r'^solutions$', views.solutionList, name='solutionList'),
    # url(r'^solutions/(?P<solution>[0-9]+)$', views.solutionDetailView.as_view(), name='solutionDetail'),
    # url(r'^solutions/add$', views.checkAdd, name='solutionAdd'),
    # url(r'^solutions/create$', views.checkCreate, name='solutionCreate'),
    # url(r'^solutions/(?P<solution>[0-9]+)/edit$', views.solutionEdit, name='solutionEdit'),
    # url(r'^solutions/(?P<solution>[0-9]+)/delete$', views.checkDelete, name='solutionDelete'),

    # feedback
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/feedbacks/add$', views.feedbackGenerate, name='feedbackAdd'),
    url(r'^tasks/(?P<task>[0-9]+)/solution_list/(?P<solution>[0-9]+)/feedbacks/send$', views.feedbackSend, name='feedbackSend')
]
