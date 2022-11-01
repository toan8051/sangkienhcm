from django import forms
from crispy_forms.helper import FormHelper
from .models import Sangkien

class SangkienForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SangkienForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True 
    # author = forms.CharField(disabled=True)
    class Meta:
        model = Sangkien
        #fields = ('description', 'document', )
        fields = [
            "donvivttp",
            "author",
            "author_2",
            "author_3",
            "cellphone",
            "idea_name",
            "content",
            "upload_file",
            "created_by",
        ]

        labels = {
            'donvivttp': 'Tên đơn vị',
            'author': 'Tác giả 1 (chủ trì)',
            "author_2": 'Tác giả 2 (đồng chủ trì)',
            "author_3": 'Tác giả 3',
            "cellphone": 'Điện thoại liên lạc (khi cần tìm hiểu thêm nội dung sáng kiến)',
            "idea_name": 'Tên sáng kiến (ghi ngắn gọn súc tích)',
            "content": 'Tóm tắt sáng kiến (tại sao làm sáng kiến này, kết quả đạt được là gì?)',
            "upload_file": 'Đính Kèm file - Bản đăng ký sáng kiến',
            "created_by": 'Người gửi sáng kiến',          
        }

        # widgets = {
        #     'author': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }


       # 'Ghi chú, đề xuất của TGV'
       # 'Người thẩm sáng kiến'
       # 'Kết quả xếp loại'
       # 'Sáng kiến đã xét'
       # 'Đề xuất cấp Tập Đoàn'
       # 'Đề xuất Sáng tạo VNPT'
       # 'Thời gian tạo sáng kiến'
       # 'Thời gian cập nhật sáng kiến'
       # 'Người cập nhật sáng kiến'