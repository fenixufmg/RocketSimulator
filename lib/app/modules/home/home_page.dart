import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

import 'widgets/items_widget.dart';
import 'home_store.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends ModularState<HomePage, HomeStore> {

  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SizedBox(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        child: Column(
          children: [
            ItemsWidget(
              items: [
                ColumnItem(
                  title: 'Geometry',
                  active: true,
                  onPressed: () => Modular.to.navigate('/home/geometry'),
                  icon: 'ruler.png',
                ),
                ColumnItem(
                  title: 'Engine',
                  active: false,
                  onPressed: () => Modular.to.navigate('/home/engine'),
                  icon: 'engine.png',
                ),
                ColumnItem(
                  title: 'Recovery',
                  active: false,
                  onPressed: () => Modular.to.navigate('/home/recovery'),
                  icon: 'parachute.png',
                ),
                ColumnItem(
                  title: 'Simulation',
                  active: false,
                  onPressed: () => Modular.to.navigate('/home/simulation'),
                  icon: 'rocket.png',
                ),
                ColumnItem(
                  title: 'Analysis',
                  active: false,
                  onPressed: () => Modular.to.navigate('/home/analysis'),
                  icon: 'bar-chart.png',
                ),
                ColumnItem(
                  title: 'Storage',
                  active: false,
                  onPressed: () => Modular.to.navigate('/home/storage'),
                  icon: 'server-storage.png',
                ),
              ],
            ),
            Container(
              width: MediaQuery.of(context).size.width,
              height: 3,
              color: AppColors.white,
            ),
            Expanded(
              child: Container(
                color: Colors.grey[100],
                child: RouterOutlet(),
              ),
            )
          ],
        ),
      ),
    );
  }

  
}