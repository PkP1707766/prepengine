-- ============================================================================
-- Storage buckets.
--
-- Before this, study material could only be a pasted external link, and a
-- student's profile photo was stored as a base-64 data URL inside the profiles
-- row (a 3 MB image became a ~4 MB text column, sent on every profile read).
-- ============================================================================

-- Study material: PDFs, notes and video files an admin uploads.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'materials', 'materials', true, 52428800,   -- 50 MB
  array['application/pdf','image/png','image/jpeg','image/webp',
        'video/mp4','video/webm','text/plain',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
)
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Profile photos.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('avatars', 'avatars', true, 3145728,   -- 3 MB
        array['image/png','image/jpeg','image/webp','image/gif'])
on conflict (id) do update
  set public = excluded.public,
      file_size_limit = excluded.file_size_limit,
      allowed_mime_types = excluded.allowed_mime_types;

-- Reset policies so this migration is re-runnable.
do $$
declare r record;
begin
  for r in
    select policyname from pg_policies
    where schemaname = 'storage' and tablename = 'objects'
      and policyname like 'jn_%'
  loop
    execute format('drop policy %I on storage.objects', r.policyname);
  end loop;
end $$;

-- Materials: world-readable (the bucket is public and links are unguessable),
-- writable only by admins.
create policy jn_materials_read on storage.objects for select
  using (bucket_id = 'materials');
create policy jn_materials_write on storage.objects for insert
  with check (bucket_id = 'materials' and public.is_admin());
create policy jn_materials_update on storage.objects for update
  using (bucket_id = 'materials' and public.is_admin())
  with check (bucket_id = 'materials' and public.is_admin());
create policy jn_materials_delete on storage.objects for delete
  using (bucket_id = 'materials' and public.is_admin());

-- Avatars: readable by anyone, but a user may only write inside a folder named
-- after their own user id — so nobody can overwrite someone else's photo.
create policy jn_avatars_read on storage.objects for select
  using (bucket_id = 'avatars');
create policy jn_avatars_write on storage.objects for insert
  with check (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
create policy jn_avatars_update on storage.objects for update
  using (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text)
  with check (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
create policy jn_avatars_delete on storage.objects for delete
  using (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
