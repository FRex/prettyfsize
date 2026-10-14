local prettyfsize = {}

function prettyfsize.prettyfsize(fsize)
    if fsize < 0 then
        return "-" .. prettyfsize.prettyfsize(-fsize)
    end
    if fsize == 1 then
        return "1 Byte"
    end
    if fsize < 1024 then
        return ("%d Bytes"):format(fsize)
    end
    if fsize < 1024 ^ 2 then
        return ("%.3f KiB"):format(fsize / 1024)
    end
    if fsize < 1024 ^ 3 then
        return ("%.3f MiB"):format(fsize / (1024 ^ 2))
    end
    if fsize < 1024 ^ 4 then
        return ("%.3f GiB"):format(fsize / (1024 ^ 3))
    end
    return ("%.3f TiB"):format(fsize / (1024 ^ 4))
end

return prettyfsize
