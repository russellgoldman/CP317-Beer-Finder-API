# coding: utf-8
from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, SmallInteger, String, Table, Text, UniqueConstraint
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import OID
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class AuthGroup(db.Model):
    __tablename__ = 'auth_group'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(80), nullable=False, unique=True)


class AuthGroupPermission(db.Model):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        db.UniqueConstraint('group_id', 'permission_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    group_id = db.Column(db.ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = db.Column(db.ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = db.relationship('AuthGroup', primaryjoin='AuthGroupPermission.group_id == AuthGroup.id', backref='auth_group_permissions')
    permission = db.relationship('AuthPermission', primaryjoin='AuthGroupPermission.permission_id == AuthPermission.id', backref='auth_group_permissions')


class AuthPermission(db.Model):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        db.UniqueConstraint('content_type_id', 'codename'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(255), nullable=False)
    content_type_id = db.Column(db.ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    codename = db.Column(db.String(100), nullable=False)

    content_type = db.relationship('DjangoContentType', primaryjoin='AuthPermission.content_type_id == DjangoContentType.id', backref='auth_permissions')


class AuthUser(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime(True))
    is_superuser = db.Column(db.Boolean, nullable=False)
    username = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    date_joined = db.Column(db.DateTime(True), nullable=False)


class AuthUserGroup(db.Model):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'group_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    group_id = db.Column(db.ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = db.relationship('AuthGroup', primaryjoin='AuthUserGroup.group_id == AuthGroup.id', backref='auth_user_groups')
    user = db.relationship('AuthUser', primaryjoin='AuthUserGroup.user_id == AuthUser.id', backref='auth_user_groups')


class AuthUserUserPermission(db.Model):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'permission_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = db.Column(db.ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    permission = db.relationship('AuthPermission', primaryjoin='AuthUserUserPermission.permission_id == AuthPermission.id', backref='auth_user_user_permissions')
    user = db.relationship('AuthUser', primaryjoin='AuthUserUserPermission.user_id == AuthUser.id', backref='auth_user_user_permissions')


class DjangoAdminLog(db.Model):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        db.CheckConstraint('action_flag >= 0'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    action_time = db.Column(db.DateTime(True), nullable=False)
    object_id = db.Column(db.Text)
    object_repr = db.Column(db.String(200), nullable=False)
    action_flag = db.Column(db.SmallInteger, nullable=False)
    change_message = db.Column(db.Text, nullable=False)
    content_type_id = db.Column(db.ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), index=True)
    user_id = db.Column(db.ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    content_type = db.relationship('DjangoContentType', primaryjoin='DjangoAdminLog.content_type_id == DjangoContentType.id', backref='django_admin_logs')
    user = db.relationship('AuthUser', primaryjoin='DjangoAdminLog.user_id == AuthUser.id', backref='django_admin_logs')


class DjangoContentType(db.Model):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        db.UniqueConstraint('app_label', 'model'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    app_label = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)


class DjangoMigration(db.Model):
    __tablename__ = 'django_migrations'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    app = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    applied = db.Column(db.DateTime(True), nullable=False)


class DjangoSession(db.Model):
    __tablename__ = 'django_session'

    session_key = db.Column(db.String(40), primary_key=True, index=True)
    session_data = db.Column(db.Text, nullable=False)
    expire_date = db.Column(db.DateTime(True), nullable=False, index=True)


class HomeBeer(db.Model):
    __tablename__ = 'home_beer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    beerName = db.Column(db.String(50), nullable=False)
    alcoholVolume = db.Column(db.Float(53), nullable=False)
    bodyType_id = db.Column(db.ForeignKey('home_bodytype.id', deferrable=True, initially='DEFERRED'), index=True)
    brand_id = db.Column(db.ForeignKey('home_brand.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    bottlePrice = db.Column(db.Float(53))
    canPrice = db.Column(db.Float(53))
    kegPrice = db.Column(db.Float(53))
    beerPhoto = db.Column(db.String(100), nullable=False)
    colour_id = db.Column(db.ForeignKey('home_colour.id', deferrable=True, initially='DEFERRED'), index=True)

    bodyType = db.relationship('HomeBodytype', primaryjoin='HomeBeer.bodyType_id == HomeBodytype.id', backref='home_beers')
    brand = db.relationship('HomeBrand', primaryjoin='HomeBeer.brand_id == HomeBrand.id', backref='home_beers')
    colour = db.relationship('HomeColour', primaryjoin='HomeBeer.colour_id == HomeColour.id', backref='home_beers')


class HomeBeerContainerType(db.Model):
    __tablename__ = 'home_beer_containerType'
    __table_args__ = (
        db.UniqueConstraint('beer_id', 'containertype_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    beer_id = db.Column(db.ForeignKey('home_beer.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    containertype_id = db.Column(db.ForeignKey('home_containertype.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    beer = db.relationship('HomeBeer', primaryjoin='HomeBeerContainerType.beer_id == HomeBeer.id', backref='home_beer_container_types')
    containertype = db.relationship('HomeContainertype', primaryjoin='HomeBeerContainerType.containertype_id == HomeContainertype.id', backref='home_beer_container_types')


class HomeBeerTaste(db.Model):
    __tablename__ = 'home_beer_taste'
    __table_args__ = (
        db.UniqueConstraint('beer_id', 'taste_id'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    beer_id = db.Column(db.ForeignKey('home_beer.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    taste_id = db.Column(db.ForeignKey('home_taste.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    beer = db.relationship('HomeBeer', primaryjoin='HomeBeerTaste.beer_id == HomeBeer.id', backref='home_beer_tastes')
    taste = db.relationship('HomeTaste', primaryjoin='HomeBeerTaste.taste_id == HomeTaste.id', backref='home_beer_tastes')


class HomeBodytype(db.Model):
    __tablename__ = 'home_bodytype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    bodyTypeName = db.Column(db.String(20), nullable=False)


class HomeBrand(db.Model):
    __tablename__ = 'home_brand'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    brandName = db.Column(db.String(50), nullable=False)
    countryOfOrigin = db.Column(db.String(50), nullable=False)


class HomeColour(db.Model):
    __tablename__ = 'home_colour'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    colourNum = db.Column(db.Integer, nullable=False)
    colourHex = db.Column(db.String(10), nullable=False)


class HomeContainertype(db.Model):
    __tablename__ = 'home_containertype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    containerTypeName = db.Column(db.String(20), nullable=False)


class HomeRating(db.Model):
    __tablename__ = 'home_rating'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    ratingValue = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(True), nullable=False)
    beer_id = db.Column(db.ForeignKey('home_beer.id', deferrable=True, initially='DEFERRED'), index=True)
    reviewText = db.Column(db.Text)

    beer = db.relationship('HomeBeer', primaryjoin='HomeRating.beer_id == HomeBeer.id', backref='home_ratings')


class HomeTaste(db.Model):
    __tablename__ = 'home_taste'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    tasteName = db.Column(db.String(50), nullable=False)
