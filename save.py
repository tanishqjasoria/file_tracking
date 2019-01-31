import numpy as np

before = {

  'one.tgz': '1234567890abcdef',

  'foo/two.tgz': '0000001111112222',

  'three.txt': '1111222233334444',

  'bar/bat/four.tgz': '6677889900112233'

}

after = {

  'five.txt': '5555555555555555',

  'one.tgz': '1234567890abcdef',

  'foo/two.tgz': 'ffffffffffffffff',

  'bar/bat/four.tgz': '6677889900112233',

  'baz/six.tgz': '6666666666666666'
  
}

np.save('metadata_before.npy', before)
np.save('metadata_after.npy', after) 