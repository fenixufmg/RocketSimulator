import 'package:flutter/material.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

import 'inputs/geometry_inputs.dart';

class GeometryItemsWidget extends StatelessWidget {
  const GeometryItemsWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      color: AppColors.white,
      height: 30,
      child: Row(
        children: [
          _button(
            message: 'Upload geometry',
            onPressed: () => GeometryInputs.upload(context),
            icon: Icons.upload,
          ),
          _button(
              message: 'Nose',
              asset: 'nose.png',
              onPressed: () => GeometryInputs.nose(context),
              icon: Icons.add),
          _button(
            message: 'Body',
            asset: 'body.png',
            onPressed: () => GeometryInputs.body(context),
            icon: Icons.add,
          ),
          _button(
            message: 'Transition',
            asset: 'transition.png',
            onPressed: () => GeometryInputs.transition(context),
            icon: Icons.add,
          ),
          _button(
            message: 'Fin',
            asset: 'fin.png',
            onPressed: () => GeometryInputs.fins(context),
            icon: Icons.add,
          ),
          _button(
            message: 'Internal component',
            asset: 'component.png',
            onPressed: () => GeometryInputs.internalComponent(context),
            icon: Icons.add,
          ),
        ],
      ),
    );
  }

  Widget _button({
    required String message,
    required void Function() onPressed,
    required IconData icon,
    String? asset,
  }) =>
      Padding(
        padding: const EdgeInsets.symmetric(vertical: 5.0),
        child: Tooltip(
          message: message,
          child: MaterialButton(
            onPressed: onPressed,
            minWidth: 10,
            child: asset != null
                ? Image(
                    image: AssetImage('assets/geometry/' + asset),
                    color: Colors.grey[500],
                    height: 16,
                  )
                : Icon(
                    icon,
                    size: 20,
                    color: Colors.grey[600],
                  ),
          ),
        ),
      );
}
