import asyncio
import json
import ast
import os
from kasa import SmartPlug, Discover

class TridentControl:
  def __init__(self):
    self.name = "Trident"
  
  #def __init__(self, newName):
  #  self.name = newName

  async def async_init(self):
    devs = await(Discover.discover())
    for key in devs:
      dev = devs[key]
      if dev.alias == self.name: 
        self.device = dev
    return self

  def __await__(self):
    return self.async_init().__await__()

def print_alias(dev):
  print(f"Discovered {dev.alias}")
  print(f"Modules: {dev.supported_modules}")

async def main():
  control = await TridentControl() 
  while not hasattr(control, 'device'):
    control = await TridentControl() 
  print(control.device)
  device = control.device
  await device.update()
  rules = await device._query_helper("count_down", "get_rules", None)
  if rules is not None:
    rule = rules["rule_list"][0]
    print(str(rule))
    rule['enable']=1
    rule['delay']=10
    rule['act']=0
    print (str(rule))
    await device._query_helper("count_down", "edit_rule", rule) 
    os.system("shutdown -h now")

if __name__ == "__main__":
  asyncio.run(main())
