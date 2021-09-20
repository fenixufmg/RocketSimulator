import 'package:flutter_modular/flutter_modular.dart';

import 'storage_page.dart';

class StorageModule extends Module {
  @override
  final List<Bind> binds = [];

  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute, child: (_, args) => StoragePage()),
  ];

}