# import pytest
# from model_bakery import baker
#
# from djavit.modules import facade
# from djavit.modules.models import Module
#
#
# @pytest.fixture
# def modules(db):
#     return [baker.make(Module, title=s) for s in 'Antes Depois'.split()]
#
#
#  def test_list_ordered_modules(modules):
#      assert list(sorted(modules, key=lambda module: module.title)) == facade.list_ordered_modules()
