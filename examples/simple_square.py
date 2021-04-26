from jubilee_controller.jubilee_controller import JubileeMotionController


if __name__ == "__main__":
    jubilee = JubileeMotionController("192.168.1.2", debug=True)

    #jubilee.home_xyu()

    jubilee.set_feedrate(300 * 60) # 300 mm/sec
    jubilee.move_xyz_absolute(z=10)
    jubilee.move_xyz_absolute(x=150, y=150)
    jubilee.move_xyz_absolute(x=150, y=200)
    jubilee.move_xyz_absolute(x=200, y=200)
    jubilee.move_xyz_absolute(x=200, y=150)
    jubilee.move_xyz_absolute(x=150, y=150, wait=True)
    jubilee.set_feedrate(10 * 60) # 10 mm/sec
