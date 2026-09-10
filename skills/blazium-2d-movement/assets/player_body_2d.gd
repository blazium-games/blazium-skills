extends CharacterBody2D
## Starter 4.3.2 / Blazium 0.6.x platformer body.
## Copy into a player scene. Do not treat this as a genre kit.

@export var speed: float = 200.0
@export var jump_velocity: float = -400.0
@export var coyote_time: float = 0.08

var _coyote: float = 0.0

func _ready() -> void:
	motion_mode = MOTION_MODE_GROUNDED
	floor_snap_length = 8.0
	up_direction = Vector2.UP

func _physics_process(delta: float) -> void:
	if is_on_floor():
		_coyote = coyote_time
	else:
		velocity += get_gravity() * delta
		_coyote = maxf(_coyote - delta, 0.0)

	if Input.is_action_just_pressed("jump") and _coyote > 0.0:
		velocity.y = jump_velocity
		_coyote = 0.0

	var dir := Input.get_axis("ui_left", "ui_right")
	velocity.x = dir * speed
	move_and_slide()
