import 'package:flutter_modular/flutter_modular.dart';

import 'geometry_page.dart';

class GeometryModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => GeometryPage()),
  ];

}