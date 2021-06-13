class Read < ApplicationRecord
  # broadcasts_to ->(read) { :reads }
  after_create_commit { broadcast_prepend_to "reads" }
  after_update_commit { broadcast_replace_to "reads" }
  after_destroy_commit { broadcast_remove_to "reads" }
end
