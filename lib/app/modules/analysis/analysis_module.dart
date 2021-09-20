import 'package:flutter_modular/flutter_modular.dart';

import 'analysis_page.dart';

class AnalysisModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => AnalysisPage()),
  ];

}