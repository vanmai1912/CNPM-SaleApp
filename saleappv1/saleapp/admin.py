from saleapp.models import Category, Product
from saleapp import db, app
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


class ProductView(ModelView):
    column_searchable_list = ['name','description']
    column_filters = ['name','price']
    can_view_details = True
    can_export = True
    column_exclude_list = ['image']
    column_labels = {
        'name':'Tên sản phẩm',
        'description':'Mô tả',
        'price': 'Giá'
    }


class StatsView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('admin/stats.html')


# class CategoryView(ModelView):
#     column_searchable_list = ['name', 'description']
#     column_filters = ['name', 'price']
#     can_view_details = True
#     can_export = True
#     column_exclude_list = ['image']

admin = Admin(app=app, name="Quan tri ban hang", template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session, name='Danh mục'))
admin.add_view(ProductView(Product, db.session, name="Sản phẩm"))
admin.add_view(StatsView(name='Thống kê'))