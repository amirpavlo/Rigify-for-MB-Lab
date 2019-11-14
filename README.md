# Rigify-for-MB-Lab

1. Download or clone the Rigify-for-MB-Lab add-on
2. Install it by copying the directory to Blender's add-on directory or by using the blender zip installer
3. Enable the Rigify add-on in blender. It comes with blender by default
4. Follow the tutorial below on how to use it with MB-Lab Character

https://www.youtube.com/watch?v=JXzxVerR2C4

TODO:
1. Verify backport to 2.79
2. generate_rig.py
  # Set "DEF-spine03" B-Bone handle
  # bpy.context.object.data.bones["DEF-spine03"].bbone_handle_type_end = 'ABSOLUTE'


NOTE:
Is it possible to maintain a single codebase that works for both Blender 2.7 and 2.8? (Yes).

c.f. https://theduckcow.com/2019/update-addons-both-blender-28-and-27-support/

https://www.youtube.com/watch?v=W8PxOFA6AFo
