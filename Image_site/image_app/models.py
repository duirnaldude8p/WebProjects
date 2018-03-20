from django.db import models
import os

# Create your models here.

# class CustomImageField(ImageField):
#     """Allows model instance to specify upload_to dynamically.

#     Model class should have a method like:

#         def get_upload_to(self, attname):
#             return 'path/to/{0}'.format(self.id)
#     """
#     def __init__(self, *args, **kwargs):
#         kwargs['upload_to'] = kwargs.get('upload_to', 'image_path')

#         try:
#             self.use_key = kwargs.pop('use_key')
#         except KeyError:
#             self.use_key = False

#         super(CustomImageField, self).__init__(*args, **kwargs)

#     def contribute_to_class(self, cls, name):
#         """Hook up events so we can access the instance."""
#         super(CustomImageField, self).contribute_to_class(cls, name)
#         dispatcher.connect(self._move_image, signal=signals.post_save, sender=cls)

#     def _move_image(self, instance=None):
#     	"""
#             Function to move the temporarily uploaded image to a more suitable directory 
#             using the model's get_upload_to() method.
#         """
#         if hasattr(instance, 'get_upload_to'):
#             src = getattr(instance, self.attname)
#             if src:
#                 m = re.match(r"%s/(.*)" % self.upload_to, src)
#                 if m:
#                     if self.use_key:
#                         dst = "%s/%d_%s" % (instance.get_upload_to(self.attname), instance.id, m.groups()[0])
#                     else:
#                         dst = "%s/%s" % (instance.get_upload_to(self.attname), m.groups()[0])
#                     basedir = "%s%s/" % (settings.MEDIA_ROOT, os.path.dirname(dst))
#                     mkpath(basedir)
#                     shutil.move("%s%s" % (settings.MEDIA_ROOT, src),"%s%s" % (settings.MEDIA_ROOT, dst))
#                     setattr(instance, self.attname, dst)
#                     instance.save()

#     def db_type(self):
#         """Required by Django for ORM."""
#         return 'varchar(100)'

def image_path(instance, filename):
	return os.path.join('static/pics/', str(instance.id), filename)


class Picture(models.Model):
	pic_name = models.CharField(max_length=10, null=True)
	pic = models.ImageField(upload_to=image_path, null=True)

	# Model Save override 
	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image = self.pic
			self.pic = None
			super(Picture, self).save(*args, **kwargs)
			self.pic = saved_image
			kwargs.pop('force_insert')

			super(Picture, self).save(*args, **kwargs)

	def __str__(self):
		return self.pic_name

	def pic_id(self):
		return self.id



		