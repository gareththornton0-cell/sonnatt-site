-- Applied to the Sonnatt Supabase project on 2026-10-11 (migration "self_serve_products").
-- Kept here as a record; the live database already has it.

-- Chatbot widgets sold to clients: one row per client site. Public visitors may read only the
-- display columns of active widgets; alert_email stays private to the team.
create table public.chat_widgets (
  id text primary key check (id ~ '^[a-z0-9][a-z0-9-]{2,40}$'),
  business text not null check (char_length(business) <= 200),
  greeting text check (char_length(greeting) <= 500),
  accent text default '#0095F7' check (accent ~ '^#[0-9A-Fa-f]{6}$'),
  faqs jsonb not null default '[]'::jsonb,
  booking_url text check (booking_url is null or booking_url ~ '^https://'),
  alert_email text check (char_length(alert_email) <= 320),
  plan text not null default 'chat' check (plan in ('chat','starter','core','demo')),
  active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.chat_widgets enable row level security;
create policy chat_widgets_team_all on public.chat_widgets for all to authenticated
  using ((select is_team())) with check ((select is_team()));
create policy chat_widgets_public_read on public.chat_widgets for select to anon using (active);
revoke all on public.chat_widgets from anon;
grant select (id, business, greeting, accent, faqs, booking_url) on public.chat_widgets to anon;

-- New lead sources: online plan signups, the free website checker and client chatbot widgets.
alter table public.website_leads drop constraint website_leads_form_name_check;
alter table public.website_leads add constraint website_leads_form_name_check
  check (form_name = any (array['contact-request','chatbot-lead','plan-signup','site-check','widget-lead']));
alter table public.website_leads add column widget_id text references public.chat_widgets(id) on delete set null;
create index website_leads_widget_id_idx on public.website_leads(widget_id);

-- Plus a 'demo' widget row (Leeds Hair Studio) used on sonnattai.com/website-chatbot/.
