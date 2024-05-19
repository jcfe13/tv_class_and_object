# 2. Import the TV class from the tv.py file
from tv import TV

# 3. Create instances of the TV class.
def test_tv():
    tv1 = TV()
    tv2 = TV()

    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)

    tv2.turn_on()
    tv2.set_channel(3)
    tv2.set_volume(2)

    # 4. Print the channel and volume level for both TVs.
