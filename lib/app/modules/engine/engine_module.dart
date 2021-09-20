import 'package:flutter_modular/flutter_modular.dart';

import 'engine_page.dart';

class EngineModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => EnginePage()),
  ];

}