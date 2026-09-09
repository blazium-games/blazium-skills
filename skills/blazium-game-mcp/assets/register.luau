-- Project-owned Streamable HTTP MCP tools.
-- JustAMCPRuntime.load_project_mcp_scripts() instantiates this script and calls register().
-- Do not prefix project tools with blazium_ (reserved).

local score = 0
local paused = false

local function runtime()
	if Engine.has_singleton("JustAMCPRuntime") then
		return Engine.get_singleton("JustAMCPRuntime")
	end
	return nil
end

local function echo(args)
	return tostring(args.text or "")
end

local function get_score(_args)
	return { score = score }
end

local function set_pause(args)
	if args.paused ~= nil then
		paused = args.paused and true or false
	else
		paused = not paused
	end
	return { paused = paused }
end

function register()
	local rt = runtime()
	if rt == nil then
		error("JustAMCP: mcp/register.luau needs the JustAMCPRuntime singleton")
	end
	rt:register_tool(
		"project_echo",
		"Echo text from this Blazium game.",
		{
			type = "object",
			properties = {
				text = { type = "string", description = "Text to echo" },
			},
			required = { "text" },
		},
		echo
	)
	rt:register_tool(
		"project_get_score",
		"Return the example score.",
		{ type = "object", properties = {} },
		get_score
	)
	rt:register_tool(
		"project_pause",
		"Set or toggle the example pause flag.",
		{
			type = "object",
			properties = {
				paused = { type = "boolean", description = "If omitted, toggle" },
			},
		},
		set_pause
	)
end
