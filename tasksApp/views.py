from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
import datetime, logging
from .models import Check, Task, Solution, CheckList, State
from django.core.mail import send_mail
from operator import itemgetter

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("This is the Tasks App")


class CheckListDetailView(generic.DetailView):
    model = CheckList
    template_name = 'tasksApp/Checklist/detail.html'


class CheckListListView(generic.ListView):
    model = CheckList
    template_name = 'tasksApp/Checklist/list.html'


def checkListAdd(request):
    template = loader.get_template('tasksApp/CheckList/add.html')

    check_list = Check.objects.all()

    context = RequestContext(request, {

        'check_list': check_list,

    })

    return HttpResponse(template.render(context))


#
#def checkListEdit(request, checklist):
 #   template = loader.get_template('tasksApp/CheckList/edit.html')
#
#    context = RequestContext(request, {
#
#        'checklist': checklist,
#
#    })
#
 #   return HttpResponse(template.render(context))


def checkListEdit(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    checkListObject = taskObject.checkList
    selected_name = request.POST['name']

    checkListObject.name = selected_name

    checkListObject.save()

    return HttpResponseRedirect(reverse('checklistTask', args={task: task}))


def checkListUpdate(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    checkListObject = taskObject.checkList
    template = loader.get_template('tasksApp/Checklist/edit.html')

    context = RequestContext(request, {

        'task': taskObject,
        'checkList': checkListObject,

    })

    return HttpResponse(template.render(context))


def checkListDelete(request, checklist):
    CheckList.objects.get(pk=checklist).delete()
    return HttpResponseRedirect(reverse('index'))


def checkListList(request):
    template = loader.get_template('tasksApp/CheckList/list.html')

    check_list = CheckList.objects.all()

    context = RequestContext(request, {

        'check_list': check_list,

    })

    return HttpResponse(template.render(context))


def checkListCreate(request):
    selected_name = request.POST['name']

    new_check_list = CheckList(name=selected_name)

    listChecks = request.POST.getlist('checks')
    new_check_list.save()

    for i in listChecks:
        check = get_object_or_404(Check, pk=i)
        new_check_list.checks.add(check)



    return HttpResponseRedirect(reverse('taskAdd'))





def checkListFill(request, solution, task):
    this_solution = Solution.objects.get(pk=solution)

    this_task = Task.objects.get(pk=task)

    states = State.objects.filter(solution=solution)

    template = loader.get_template('tasksApp/Solution/checklistfill.html')

    context = RequestContext(request, {

        'task': this_task,

        'solution': this_solution,

        'states': states,

    })

    return HttpResponse(template.render(context))


def checklistTask(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    check_list = taskObject.checkList
    checks = check_list.checks

    template = loader.get_template('tasksApp/Task/checklist.html')

    context = RequestContext(request, {

        'task': taskObject,

        'check_list': checks,

    })

    return HttpResponse(template.render(context))


def CheckDetailView(request, task, check):
    checkObject = get_object_or_404(Check, pk=check)

    template = loader.get_template('tasksApp/Check/detail.html')

    context = RequestContext(request, {

        'task': task,

        'check': checkObject,

    })

    return HttpResponse(template.render(context))


def checkAdd(request, task):
    taskObject = get_object_or_404(Task, pk=task)

    template = loader.get_template('tasksApp/Check/add.html')

    context = RequestContext(request, {

        'task': taskObject,

    })

    return HttpResponse(template.render(context))


def checkAddExisting(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    checkList = Check.objects.all()

    template = loader.get_template('tasksApp/Check/add_existing.html')

    context = RequestContext(request, {

        'task': taskObject,
        'check_list': checkList,

    })

    return HttpResponse(template.render(context))


def checkAddExistingAction(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    listChecks = request.POST.getlist('checks')
    logger.error(listChecks)
    for i in listChecks:
        check = get_object_or_404(Check, pk=i)
        taskObject.checkList.checks.add(check)

    return HttpResponseRedirect(reverse('checklistTask', args={task: task}))


def checkCreate(request, task):
    taskObject = get_object_or_404(Task, pk=task)
    selected_name = request.POST['name']
    selected_description = request.POST['description']
    solution_list = Solution.objects.filter(task=task)

    new_check = Check(name=selected_name, description=selected_description)

    new_check.save()

    if len(solution_list) >=1 :
        for solution in solution_list:
            new_state=State(value=False, solution=solution, chk=new_check)
            new_state.save()

    taskObject.checkList.checks.add(get_object_or_404(Check, pk=new_check.id))

    return HttpResponseRedirect(reverse('checklistTask', args={task: task}))

#To create a new check when creating a new task
def checkCreateNoTask(request):
    selected_name = request.POST['name']
    selected_description = request.POST['description']

    new_check = Check(name=selected_name, description=selected_description)

    new_check.save()

    return HttpResponseRedirect(reverse('checkListAdd'))

def checkAddNoTask(request):

    template = loader.get_template('tasksApp/Check/add_notask.html')

    return HttpResponse(template.render(RequestContext(request)))


def checkUpdate(request, task, check):
    checkObject = get_object_or_404(Check, pk=check)
    selected_name = request.POST['name']
    selected_description = request.POST['description']

    checkObject.name = selected_name
    checkObject.description = selected_description

    checkObject.save()

    return HttpResponseRedirect(reverse('checklistTask', args={task: task}))


def checkEdit(request, task, check):
    taskObject = get_object_or_404(Task, pk=task)
    checkObject = get_object_or_404(Check, pk=check)
    template = loader.get_template('tasksApp/Check/edit.html')

    context = RequestContext(request, {

        'task': taskObject,
        'check': checkObject,

    })

    return HttpResponse(template.render(context))


def checkDelete(request, task, check):
    Check.objects.get(pk=check).delete()
    State.objects.filter(chk=check).delete()
    return HttpResponseRedirect(reverse('checklistTask', args={task: task}))


def taskList(request):
    task_list = Task.objects.all()
    solution_list = Solution.objects.all()
    template = loader.get_template('tasksApp/Task/list.html')

    context = RequestContext(request, {
        'solution': solution_list,
        'task_list': task_list,

    })

    return HttpResponse(template.render(context))


class TaskDetailView(generic.DetailView):
    model = Task

    template_name = 'tasksApp/Task/detail.html'


def taskAdd(request):
    checklist_list = CheckList.objects.all()

    template = loader.get_template('tasksApp/Task/add.html')

    context = RequestContext(request, {

        'checklist_list': checklist_list,

    })

    return HttpResponse(template.render(context))


def taskCreate(request):
    selected_name = request.POST['name']

    selected_description = request.POST['description']
    selected_feedb_templ_1 = request.POST['feedb_templ_1']
    selected_feedb_templ_2 = request.POST['feedb_templ_2']

    request_checklist_ID = request.POST['checklist']
    selected_checklist = CheckList.objects.get(pk=request_checklist_ID)

    new_task = Task(name=selected_name, description=selected_description, checkList=selected_checklist, feedb_templ_1=
                    selected_feedb_templ_1, feedb_templ_2=selected_feedb_templ_2)

    new_task.save()

    return HttpResponseRedirect(reverse('index'))


def taskEdit(request, task):
    template = loader.get_template('tasksApp/Task/edit.html')

    taskObject = get_object_or_404(Task, pk=task)
    checklist_list = CheckList.objects.all()

    context = RequestContext(request, {

        'task': taskObject,
        'checklist_list': checklist_list,

    })

    return HttpResponse(template.render(context))

def actionTaskUpdate(request, task):
    selected_task = Task.objects.get(pk=task)
    selected_checklist = CheckList.objects.get(pk=request.POST['checklistEdited'])

    selected_task.name = request.POST['nameEdited']
    selected_task.description = request.POST['descriptionEdited']
    selected_task.feedb_templ_1 = request.POST['feedb_templ_1Edited']
    selected_task.feedb_templ_2 = request.POST['feedb_templ_2Edited']
    selected_task.checkList = selected_checklist
    selected_task.save()

    return HttpResponseRedirect(reverse('index'))

def deleteTask(request, task):
    Task.objects.get(pk=task).delete()

    return HttpResponseRedirect(reverse('index'))


def TaskSolutionList(request, task):
    solution_list = Solution.objects.filter(task=task)
    task = Task.objects.get(pk=task)

    # if len(solution_list) == 0:
    #  raise Http404("Task does not exist")

    template = loader.get_template('tasksApp/Solution/list_tasked.html')

    context = RequestContext(request, {

        'task': task,

        'solution_list': solution_list,

    })

    return HttpResponse(template.render(context))


def AllSolutionList(request):
    solution_list = Solution.objects.all()

    template = loader.get_template('tasksApp/Solution/list_all.html')
    # if len(solution_list) == 0:
    # return HttpResponseRedirect(reverse('SolutionList', args=task))ttp404("TTo.html')

    context = RequestContext(request, {

        'solution_list': solution_list,

    })

    return HttpResponse(template.render(context))


def solutionDetaiView(request, task, solution):
    solution_object = get_object_or_404(Solution, pk=solution)

    template = loader.get_template('tasksApp/Solution/detail.html')

    context = RequestContext(request, {

        'task': task,

        'solution': solution_object,

    })

    return HttpResponse(template.render(context))

"""def solutionAddAmount(request, task):
    template = loader.get_template('tasksApp/Solution/number_of_new.html')

    context = RequestContext(request, {

        'task': task,

    })

    return HttpResponse(template.render(context))"""


def solutionAdd(request, task):
    template = loader.get_template('tasksApp/Solution/add.html')
    task = Task.objects.get(pk=task)

    context = RequestContext(request, {

        'task': task,

    })

    return HttpResponse(template.render(context))


def solutionUpdate(request, task, solution):
    template = loader.get_template('tasksApp/Solution/update.html')
    solution = Solution.objects.get(pk=solution)

    context = RequestContext(request, {

        'solution': solution,

    })

    return HttpResponse(template.render(context))



def actionSolutionUpdate(request, task, solution):
    selected_solution = Solution.objects.get(pk=solution)
    selected_solution.content = request.POST['contentEdited']
    selected_solution.student_email = request.POST['emailEdited']
    selected_solution.save()

    return HttpResponseRedirect(reverse('TaskSolutionList', args={task: task}))


def solutionCreate(request, task):
    selected_content = ""
    selected_mails=request.POST['emails'].split("\n")
    selected_task = Task.objects.get(pk=task)

    for selected_mail in selected_mails:
        new_solution = Solution(creation_date=datetime.datetime.now(), content=selected_content, task=selected_task,
                            student_email=selected_mail)
        new_solution.save()

        if selected_task.checkList:
            for check in selected_task.checkList.checks.all():
                new_state = State(solution=new_solution, chk=check)
                new_state.save()

    return HttpResponseRedirect(reverse('TaskSolutionList', args={task: task}))


def solutionDelete(request, solution):
    Solution.objects.get(pk=solution).delete()
    return HttpResponseRedirect(reverse('AllSolutionList'))


def solutionDeleteTasked(request, task, solution ):
    Solution.objects.get(pk=solution).delete()
    return HttpResponseRedirect(reverse('TaskSolutionList', args={task: task}))


def editStates(request, task, solution):
    state_list=State.objects.filter(solution=solution)
    for i in range(len(state_list)):
        try:
            request.POST['checkbox' + str(state_list[i].id)]
            state_list[i].value=True
        except:
            state_list[i].value=False
        state_list[i].save()



    return HttpResponseRedirect(reverse('TaskSolutionList', args={task: task}))


def feedbackGenerate(request, task, solution):
    template = loader.get_template('tasksApp/Feedback/generate.html')
    solution = Solution.objects.get(pk=solution)
    task = Task.objects.get(pk=task)

    state_list = State.objects.filter(solution=solution, value=True)

    context = RequestContext(request, {

        'task': task,

        'solution': solution,

        'state_list': state_list,

    })

    return HttpResponse(template.render(context))

def feedbackSend(request, task, solution):
    selected_solution = Solution.objects.get(pk=solution)
    selected_task = Task.objects.get(pk=task)

    content = request.POST['content']


    send_mail('feedback for '+selected_task.name, content, 'from@example.com',
    [selected_solution.student_email], fail_silently=False)

    return HttpResponseRedirect(reverse('index'))