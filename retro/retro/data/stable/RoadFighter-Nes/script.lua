function digit(value)
  if value < 0 then
    return 0
  end
  return value
end

oldvalue = 0

function reward()
  value = digit(data.score0)
  value = value + digit(data.score1)
  newvalue = value - oldvalue
  oldvalue = value
  return digit(newvalue)
end
