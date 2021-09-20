import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

import '../../../../../shared/widgets/general_dialog.dart';

class UploadInput extends StatelessWidget {
  const UploadInput({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GeneralDialog(
      title: 'Upload Geometry',
      alertMessage: 'Not implemented',
      content: SizedBox(width: 0.0, height: 0.0,),
      cancel: () => Modular.to.pop(),
    );
  }
}
