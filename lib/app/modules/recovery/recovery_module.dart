import 'package:flutter_modular/flutter_modular.dart';

import 'recovery_page.dart';

class RecoveryModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => RecoveryPage()),
  ];

}