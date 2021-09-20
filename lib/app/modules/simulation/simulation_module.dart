import 'package:flutter_modular/flutter_modular.dart';

import 'simulation_page.dart';

class SimulationModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => SimulationPage()),
  ];

}