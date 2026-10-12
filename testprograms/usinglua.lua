local prettyfsize = dofile "lua/prettyfsize.lua"
local io = require "io"

local outf = io.open("conout$", "wb")

if select(2, ...) == "to" then
    for fsize = tonumber((select(1, ...))), tonumber((select(3, ...))) do
        io.write(prettyfsize.prettyfsize(fsize) .. "\n")
    end
end
