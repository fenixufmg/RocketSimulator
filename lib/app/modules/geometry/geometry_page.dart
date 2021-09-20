import 'package:flutter/material.dart';
import 'package:rocket_simulator/app/modules/geometry/widgets/geometry_items_widget.dart';
import 'package:rocket_simulator/app/modules/geometry/widgets/rocket_information_widget.dart';
import 'package:rocket_simulator/app/modules/geometry/widgets/rocket_overview_information_widget.dart';

import 'widgets/rocket_view.dart';

class GeometryPage extends StatelessWidget {
  const GeometryPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        GeometryItemsWidget(),
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Stack(
              children: [
                RocketView(),
                RocketInformationWidget(),
                RocketOverviewInformationWidget(),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
