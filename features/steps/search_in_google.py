from behave import given, then, when, step
from selenium import webdriver


@given(u'que a página do Google seja apresentada')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.google.com')

@when(u'eu inserir um texto na caixa de busca')
def step_impl(context):
    search_field = context.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
    search_field.send_keys('Verity')


@when(u'acionar o botão Pesquisar')
def step_impl(context):
    form = context.browser.find_element_by_xpath('//*[@id="tsf"]')
    form.submit()


@then(u'devo visualizar os resultados da busca')
def step_impl(context):
    assert 'Verity Group' in context.browser.page_source
