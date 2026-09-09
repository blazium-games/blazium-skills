extends Node

## Project-owned Streamable HTTP MCP tools.
## JustAMCPRuntime.load_project_mcp_scripts() instantiates this script and calls register().
## Use the engine singleton — JustAMCPRuntime cannot be constructed with .new().
## Do not prefix project tools with blazium_ (reserved).

var _score := 0
var _paused := false

func register() -> void:
	var runtime := _runtime()
	if runtime == null:
		push_error("JustAMCP: mcp/register.gd needs the JustAMCPRuntime singleton")
		return

	runtime.register_tool(
		"project_echo",
		"Echo text from this Blazium game.",
		{
			"type": "object",
			"properties": {
				"text": {"type": "string", "description": "Text to echo"},
			},
			"required": ["text"],
		},
		Callable(self, "_echo")
	)
	runtime.register_tool(
		"project_get_score",
		"Return the example score.",
		{"type": "object", "properties": {}},
		Callable(self, "_get_score")
	)
	runtime.register_tool(
		"project_pause",
		"Set or toggle the example pause flag.",
		{
			"type": "object",
			"properties": {
				"paused": {"type": "boolean", "description": "If omitted, toggle"},
			},
		},
		Callable(self, "_pause")
	)

func _runtime() -> Object:
	if Engine.has_singleton("JustAMCPRuntime"):
		return Engine.get_singleton("JustAMCPRuntime")
	return null

func _echo(args: Dictionary) -> String:
	return str(args.get("text", ""))

func _get_score(_args: Dictionary) -> Dictionary:
	return {"score": _score}

func _pause(args: Dictionary) -> Dictionary:
	if args.has("paused"):
		_paused = bool(args["paused"])
	else:
		_paused = not _paused
	return {"paused": _paused}
