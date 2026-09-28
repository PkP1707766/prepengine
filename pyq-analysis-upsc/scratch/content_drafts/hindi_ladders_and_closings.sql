with m(en, hi) as (values
  ('Only one', 'केवल एक'),
  ('Only two', 'केवल दो'),
  ('Only three', 'केवल तीन'),
  ('All three', 'सभी तीन'),
  ('All four', 'सभी चार'),
  ('None', 'कोई नहीं'),
  ('Only one pair', 'केवल एक युग्म'),
  ('Only two pairs', 'केवल दो युग्म'),
  ('Only three pairs', 'केवल तीन युग्म'),
  ('All three pairs', 'सभी तीन युग्म'),
  ('All four pairs', 'सभी चार युग्म'),
  ('None of the pairs', 'कोई भी युग्म नहीं'),
  ('Both 1 and 2', '1 और 2 दोनों'),
  ('Neither 1 nor 2', 'न तो 1, न ही 2'),
  ('Both I and II', 'I और II दोनों'),
  ('Neither I nor II', 'न तो I, न ही II'),
  ('Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I', 'कथन-I और कथन-II दोनों सही हैं और कथन-II, कथन-I की सही व्याख्या है'),
  ('Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I', 'कथन-I और कथन-II दोनों सही हैं, किंतु कथन-II, कथन-I की सही व्याख्या नहीं है'),
  ('Statement-I is correct but Statement-II is incorrect', 'कथन-I सही है, किंतु कथन-II गलत है'),
  ('Statement-I is incorrect but Statement-II is correct', 'कथन-I गलत है, किंतु कथन-II सही है'),
  ('Both Statement II and Statement III are correct and both of them explain Statement I', 'कथन-II और कथन-III दोनों सही हैं और ये दोनों कथन-I की व्याख्या करते हैं'),
  ('Both Statement II and Statement III are correct but only one of them explains Statement I', 'कथन-II और कथन-III दोनों सही हैं, किंतु इनमें से केवल एक ही कथन-I की व्याख्या करता है'),
  ('Only one of the Statements II and III is correct and that explains Statement I', 'कथन-II और कथन-III में से केवल एक सही है और वही कथन-I की व्याख्या करता है'),
  ('Neither Statement II nor Statement III is correct', 'न तो कथन-II सही है, न ही कथन-III'),
  ('1 only', 'केवल 1'),
  ('2 only', 'केवल 2'),
  ('3 only', 'केवल 3'),
  ('1 and 2', '1 और 2'),
  ('2 and 3', '2 और 3'),
  ('1 and 3', '1 और 3'),
  ('1 and 2 only', 'केवल 1 और 2'),
  ('2 and 3 only', 'केवल 2 और 3'),
  ('1 and 3 only', 'केवल 1 और 3'),
  ('1, 2 and 3', '1, 2 और 3'),
  ('I only', 'केवल I'),
  ('II only', 'केवल II'),
  ('III only', 'केवल III'),
  ('I and II only', 'केवल I और II'),
  ('II and III only', 'केवल II और III'),
  ('I and III only', 'केवल I और III'),
  ('I, II and III', 'I, II और III')
)
update public.questions q set options = (
    select jsonb_agg(case when m.hi is not null then o.v || jsonb_build_object('body_hi', m.hi) else o.v end order by o.ord)
    from jsonb_array_elements(q.options) with ordinality o(v, ord) left join m on m.en = o.v->>'body'),
  updated_at = now()
where q.exam_category = 'upsc' and coalesce((q.question_data->>'fixed_option_order')::boolean, false);

with c(en, hi) as (values
  ('How many of the above statements are correct?', 'उपर्युक्त में से कितने कथन सही हैं?'),
  ('Which of the statements given above is/are correct?', 'उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?'),
  ('How many of the pairs given above are correctly matched?', 'उपर्युक्त में से कितने युग्म सही सुमेलित हैं?'),
  ('Which one of the following is correct in respect of the above statements?', 'उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा एक सही है?'),
  ('Select the correct answer using the code given below:', 'नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:'),
  ('Select the correct answer using the codes given below:', 'नीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:'),
  ('Which of the pairs given above is/are correctly matched?', 'उपर्युक्त युग्मों में से कौन-सा/से सही सुमेलित है/हैं?'),
  ('Select the correct order using the code given below:', 'नीचे दिए गए कूट का प्रयोग कर सही क्रम चुनिए:')
)
update public.questions q set question_data = q.question_data || jsonb_build_object('closing_hi', c.hi), updated_at = now()
from c where q.exam_category = 'upsc' and q.question_data->>'closing' = c.en;
