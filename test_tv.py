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
    print(f"\ntv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")

# 5. Call the test_tv function to execute the code