from fastrunner import models


def get_counter(model, pk=None):
    """
    统计相关表长度
    """
    if pk:
        return model.objects.filter(project__id=pk).count()
    else:
        return model.objects.count()


def get_project_detail(pk):
    """
    项目详细统计信息
    """
    api_count = get_counter(models.API, pk=pk)
    case_count = get_counter(models.Case, pk=pk)
    team_count = get_counter(models.Team, pk=pk)
    config_count = get_counter(models.Config, pk=pk)

    return {
        "api_count": api_count,
        "suite_count": 0,
        "case_count": case_count,
        "team_count": team_count,
        "config_count": config_count
    }


def project_init(project):
    """
    新建项目初始化
    """
    # 自动生成默认debugtalk.py
    models.Debugtalk.objects.create(project=project)
    # 自动生成API tree
    models.Relation.objects.create(project=project)
    # 自动生成Test Tree
    models.Relation.objects.create(project=project, type=2)


def project_end(project):
    """
    删除项目相关表 filter不会报异常 最好不用get
    """
    models.Debugtalk.objects.filter(project=project).delete()
    models.Team.objects.filter(project=project).delete()
    models.Config.objects.filter(project=project).delete()
    models.API.objects.filter(project=project).delete()
    models.Relation.objects.filter(project=project).delete()

    case = models.Case.objects.filter(project=project).values_list('id')

    for case_id in case:
        models.CaseStep.objects.filter(case__id=case_id).delete()


def tree_end(params, project):
    """
    project: Project Model
    params: {
        node: int,
        type: int
    }
    """
    type = params['type']
    node = params['node']

    if type == 1:
        models.API.objects. \
            filter(relation=node, project=project).delete()
    # remove node testcase
    elif type == 2:
        case = models.Case.objects. \
            filter(relation=node, project=project).values_list('id')

        for case_id in case:
            models.CaseStep.objects.filter(case__id=case_id).delete()