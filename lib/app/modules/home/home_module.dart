 import 'package:flutter_modular/flutter_modular.dart';
import 'package:rocket_simulator/app/modules/storage/storage_module.dart';
 
import '../analysis/analysis_module.dart';
import '../engine/engine_module.dart';
import '../geometry/geometry_module.dart';
import '../recovery/recovery_module.dart';
import '../simulation/simulation_module.dart';
 import '../home/home_store.dart'; 
 
 import 'home_page.dart';
  
 class HomeModule extends Module {
   @override
   final List<Bind> binds = [
  Bind.lazySingleton((i) => HomeStore()),
  ];
 
  @override
  final List<ModularRoute> routes = [
    ChildRoute(Modular.initialRoute,
      child: (_, args) => HomePage(),
      children: [
        ModuleRoute('/geometry', module: GeometryModule()),
        ModuleRoute('/engine', module: EngineModule()),
        ModuleRoute('/recovery', module: RecoveryModule()),
        ModuleRoute('/simulation', module: SimulationModule()),
        ModuleRoute('/analysis', module: AnalysisModule()),
        ModuleRoute('/storage', module: StorageModule()),
      ]),
  ];
 }