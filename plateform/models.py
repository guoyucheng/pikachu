# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Platform(models.Model):
    #id =  #db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    logo_url = models.CharField(default="", max_length=1024, db_index=True)#db.Column(db.String(254))
    #platform_lives = db.relationship('PlatformLive', backref='platform')
    #平台是否已开通
    is_used = models.BooleanField(verbose_name=u"平台是否已开通", default=False)#db.Column(db.Boolean, default=False)
    # 对于平台的第几次请求
    newest_index = models.IntegerField(verbose_name=u"对于平台的第几次请求", default=0)#db.Column(db.Integer)
    #App下载地址
    download_app = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    source = models.IntegerField(verbose_name=u"数据源", default=0)#0: 秋名山,1:jianhuangshi
    source_id = models.IntegerField(verbose_name=u"所在数据源对应的平台ID", default=0)
    update_at = models.IntegerField(verbose_name="更新时间戳", default=0)
    is_default = models.BooleanField(verbose_name=u"首页默认")
    # def to_dict(self):
    #     platform_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}  
    #     return platform_dict

    class Meta:
        db_table = "platform"
        verbose_name = u'platform'
        verbose_name_plural = u'platform'


class PlatformLive(models.Model):
    #id = #db.Column(db.Integer, primary_key=True, autoincrement=True)
    zhubo_name = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    header_img = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    rtmp_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    flv_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    m3u8_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    online_users = models.IntegerField(verbose_name=u"在线人数", default=0)#db.Column(db.Integer)
    #直播间是否有效，默认是True有效的
    is_used = models.BooleanField(verbose_name=u"直播间是否有效", default=True)#db.Column(db.Boolean, default=True)
    # 对于平台的第几次请求
    request_id = models.IntegerField(verbose_name=u"对于平台的第几次请求", default=0)#db.Column(db.Integer)
    platform = models.ForeignKey(Platform,verbose_name="平台") #db.Column(db.Integer, db.ForeignKey('platform.id'))    
    #是否付费房间
    fee = models.BooleanField(verbose_name=u"是否付费", default=False) #db.Column(db.Boolean, default=False)

    # def to_dict(self):
    #     platform_live_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}  
    #     return platform_live_dict
    class Meta:
        db_table = "platform_live"
        verbose_name = u'platform_live'
        verbose_name_plural = u'platform_live'


class QMSPlatformLive(models.Model):
    #id = #db.Column(db.Integer, primary_key=True, autoincrement=True)

    zhubo_name = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    header_img = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    url = models.CharField(null=False, max_length=1024, db_index=True)
    # rtmp_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    # flv_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    # m3u8_url = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(1024))
    online_users = models.IntegerField(verbose_name=u"在线人数", default=0)#db.Column(db.Integer)
    #直播间是否有效，默认是True有效的
    # 对于平台的第几次请求
    #request_id = models.IntegerField(verbose_name=u"对于平台的第几次请求", default=0)#db.Column(db.Integer)
    platform = models.ForeignKey(Platform,verbose_name="平台") #db.Column(db.Integer, db.ForeignKey('platform.id'))    
    #是否付费房间
    fee = models.BooleanField(verbose_name=u"是否付费", default=False) #db.Column(db.Boolean, default=False)
    host_id = models.IntegerField(verbose_name=u"房间id", default=0)
    is_used = models.BooleanField(default=True)
    # def to_dict(self):
    #     platform_live_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}  
    #     return platform_live_dict
    class Meta:
        db_table = "qms_platform_live"
        verbose_name = u'qms_platform_live'
        verbose_name_plural = u'qms_platform_live'

class Ad(models.Model):
    name = models.CharField(null=False, max_length=1024, db_index=True)#db.Column(db.String(254))
    is_used = models.BooleanField(default=True)
    url = models.CharField(null=False, max_length=1024, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ad"
        verbose_name = u'ad'
        verbose_name_plural = u'ad'
    