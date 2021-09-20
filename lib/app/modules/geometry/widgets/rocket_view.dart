import 'package:flutter/material.dart';
import 'package:flutter_cube/flutter_cube.dart';

class RocketView extends StatefulWidget {
  const RocketView({Key? key}) : super(key: key);

  @override
  _RocketViewState createState() => _RocketViewState();
}

class _RocketViewState extends State<RocketView> {

  @override
  Widget build(BuildContext context) {
    return Cube(
      onSceneCreated: (Scene scene) {
        final Object cube = Object(
          position: Vector3(0, -5, 0)..scale(1),
          scale: Vector3(20, 20, 20),
          rotation: Vector3(-90, 0, 0),
          fileName: 'assets/geometries/rocket.obj',
        );
        scene.world.add(cube);
      },
    );
  }
}
