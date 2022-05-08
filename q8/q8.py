
with open('q8.txt', 'r') as f:
    notebook = f.readlines()
    entries = []
    for entry in notebook:
        entries.append(entry.strip())


outputValues = []
for entry in entries:
    inputs = entry.split('|')[0].split()
    outputs = entry.split('|')[1].split()
    signalMappings = {}
    nonUniqueSignals = []
    for signal in inputs:
      if len(signal) == 2:
        # 1
        signalMappings[1] = signal
      elif len(signal) == 3:
        # 7
        signalMappings[7] = signal
      elif len(signal) == 4:
        # 4
        signalMappings[4] = signal
      elif len(signal) == 7:
        #8
        signalMappings[8] = signal
      else:
        nonUniqueSignals.append(signal)
    
  
    for signal in nonUniqueSignals:
      matched_list_one = [characters in [char for char in signal] for characters in signalMappings[1]]
      matched_list_four = [characters in [char for char in signal] for characters in signalMappings[4]]
      matched_list_seven = [characters in [char for char in signal] for characters in signalMappings[7]]
      matched_list_eight = [characters in [char for char in signal] for characters in signalMappings[8]]
      if len(signal) == 5:
        #2, 3, 5
          matched_list = []
          if all(matched_list_one):
            signalMappings[3] = signal
          elif matched_list_four.count(True) == 2:
            signalMappings[2] = signal
          else:
            signalMappings[5] = signal
      else:
        #0, 6, 9
        if not all(matched_list_one):
          signalMappings[6] = signal
        elif all(matched_list_four):
          signalMappings[9] = signal
        else:
          signalMappings[0] = signal

    outputNumber = ""

    for output in outputs:
      for key in signalMappings:
        if len(signalMappings[key]) == len(output):
          if all([characters in [char for char in signalMappings[key]] for characters in output]):
                outputNumber += str(key)

    outputValues.append(int(outputNumber))

print(sum(outputValues))

