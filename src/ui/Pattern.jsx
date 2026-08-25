import { Fragment } from "react";

/**
 * Render a translated pattern that carries a value inside it.
 *
 * A bolded value does not land in the same place in both languages — English
 * opens with "You skipped 4 questions" and Hindi closes with "4 सवाल छोड़ दिए"
 * — so the sentence cannot be built from fixed pieces around a <b>. The pattern
 * marks the bolded value {x} and a second, unbolded one {y}, and this splits on
 * them wherever the translator chose to put them.
 *
 * Anything else that varies (an optional clause, a number that is not bolded)
 * should be substituted into the pattern string BEFORE it gets here, with its
 * own placeholder — never by reaching for punctuation, because the sentence
 * ends in a danda in Hindi and a full stop in English.
 */
export default function Pattern({ text, x, y }) {
  const out = [];
  String(text).split("{x}").forEach((chunk, ci) => {
    if (ci > 0) out.push(<b key={"x" + ci}>{x}</b>);
    chunk.split("{y}").forEach((piece, pi) => {
      if (pi > 0) out.push(<Fragment key={"y" + ci + pi}>{y}</Fragment>);
      if (piece) out.push(<Fragment key={"t" + ci + pi}>{piece}</Fragment>);
    });
  });
  return out;
}
