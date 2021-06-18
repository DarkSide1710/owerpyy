from django.urls import path

from .apiviews import login,survey_update,survey_create, survey_view, active_survey_view,question_create,question_update,choice_create,choice_update,answer_create,answer_view,answer_update

app_name = 'surveysApp'
urlpatterns = [
    path('login/', login, name='login'),
    # Опросы (surveys)
    path('surveysApp/create/', survey_create, name='survey_create'),
    path('surveysApp/update/<int:survey_id>/', survey_update, name='survey_update'),
    path('surveysApp/view/', survey_view, name='survey_view'),
    path('surveysApp/view/active/', active_survey_view, name='active_survey_view'),
    # Вопрос (question)
    path('question/create/', question_create, name='question_create'),
    path('question/update/<int:question_id>/', question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', answer_update, name='answer_update')

]

