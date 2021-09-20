import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

import 'dialogs/body_input.dart';
import 'dialogs/fin_input.dart';
import 'dialogs/internal_component_input.dart';
import 'dialogs/nose_input.dart';
import 'dialogs/transition_input.dart';
import 'dialogs/upload_input.dart';

class GeometryInputs {

  static void upload(BuildContext context) => showDialog(
    context: context,
    builder: (context) => UploadInput(),
  );

  static void nose(BuildContext context) => showDialog(
    context: context,
    builder: (context) => NoseInput(),
  );

  static void body(BuildContext context) => showDialog(
    context: context,
    builder: (context) => BodyInput(),
  );

  static void transition(BuildContext context) => showDialog(
    context: context,
    builder: (context) => TransitionInput(),
  );

  static void fins(BuildContext context) => showDialog(
    context: context,
    builder: (context) => FinInput(),
  );

  static void internalComponent(BuildContext context) => showDialog(
    context: context,
    builder: (context) => InternalComponentInput(),
  );
}