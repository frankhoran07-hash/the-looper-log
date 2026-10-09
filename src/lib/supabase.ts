import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://xrdxysgnjrtvvvovozkb.supabase.co';
const supabaseAnonKey = 'sb_publishable_nXENTV7fBGIj75cm40LCrA_HX0XsgDW';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);